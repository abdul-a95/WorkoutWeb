from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from WebAppProject.models import Category,Post
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.files.uploadedfile import SimpleUploadedFile

class GeneralTests(TestCase):
    def test_serving_static_files(self):
        result = finders.find('images/default-profile.jpg')
        self.assertIsNotNone(result)

    # tests if slug field works
    def test_does_slug_field_work(self):
        from WebAppProject.models import Category
        cat = Category(name='how do i create a slug in django')
        cat.save()
        self.assertEqual(cat.slug,'how-do-i-create-a-slug-in-django')

class ModelTests(TestCase):
    def setUp(self):
        try:
            from populate_workoutweb import populate
            populate()
        except ImportError:
            print('The module populate_workoutweb does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

    def get_category(self, name):

        from WebAppProject.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat

    def get_post(self, title):

        from WebAppProject.models import Post
        try:
            post = Post.objects.get(title=title)
        except Post.DoesNotExist:
            post = None
        return post


    def test_python_cat_added(self):
        cat = self.get_category('Supplements')
        self.assertIsNotNone(cat)

    def test_python_post_added(self):
        post = self.get_post('New protein')
        self.assertIsNotNone(post)

    def test_python_post_with_views(self):
        post = self.get_post('Ab Workout')

        self.assertEquals(post.views, 18)

    def test_python_post_with_likes(self):
        post = self.get_post('Ab Workout')

        self.assertEquals(post.likes, 7)

class ModelCreations(TestCase):
    def test_create_a_new_category(self):
        cat = Category(name="Health")
        cat.save()

        # Check category is in database
        categories_in_database = Category.objects.all()
        self.assertEquals(len(categories_in_database), 1)
        only_poll_in_database = categories_in_database[0]
        self.assertEquals(only_poll_in_database, cat)

    def test_create_pages_for_categories(self):
        cat = Category(name="Health")
        cat.save()

        # create 2 pages for category python
        health_post = Post()
        health_post.category = cat
        health_post.title = "Smoking is bad"
        health_post.views = 20
        health_post.likes = 5
        health_post.save()

        health_post2 = Post()
        health_post2.category = cat
        health_post2.title = "fruit is good"
        health_post2.views = 100
        health_post2.likes = 50
        health_post2.save()

        # Check if they both were saved
        health_posts = cat.post_set.all()
        self.assertEquals(health_posts.count(), 2)

        # Check if they were saved properly
        first_post = health_posts[0]
        self.assertEquals(first_post.title, "Smoking is bad")
        self.assertEquals(first_post.views,20 )


class IndexPageTests(TestCase):
    def test_index_contains_welcome_message(self):
        # Check if there is the message 'Rango Says'
        # Chapter 4
        response = self.client.get(reverse('workoutweb:index'))
        self.assertIn(b'Welcome to Workout Web', response.content)

    def test_index_using_template(self):
        # Check the template used to render index page
        # Chapter 4
        response = self.client.get(reverse('workoutweb:index'))
        self.assertTemplateUsed(response, 'workoutweb/index.html')

    def test_index_aboutpage_link(self):
        response = self.client.get(reverse("workoutweb:index"))
        self.assertContains(response, '<a href="%s">About Us</a>' % reverse("workoutweb:about"), html=True)

    def test_index_nearestgym_link(self):
        response = self.client.get(reverse("workoutweb:index"))
        self.assertContains(response, '<a href="%s">Find Nearest Gym</a>' % reverse("workoutweb:nearest_gym"),
                            html=True)


class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('workoutweb:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

class TestCategories(TestCase):
    def test_index_view_with_categories(self):
        """
        Check to make sure that the index has categories displayed
        """
        add_cat('test')
        add_cat('temp')
        add_cat('tmp')
        add_cat('tmp test temp')
        response = self.client.get(reverse('workoutweb:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")
        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 4)

class FormsTest(TestCase):
    def setUp(self):
        try:
            from forms import CommentForm
            from forms import PostForm
            from forms import ContactForm
            from forms import UserProfileForm

        except ImportError:
            print('The module forms does not exist')
        except NameError:
            print('The class PageForm does not exist or is not correct')
        except:
            print('Something else went wrong :-(')

    pass

class Imagetest(TestCase):
    def test_upload_image(self):
        # Create fake user and image to upload to register user
        image = SimpleUploadedFile("testuser.jpg", "file_content", content_type="image/jpeg")
        try:
            response = self.client.post(reverse('register'),
                                    {'username': 'testuser', 'password': 'test1234',
                                     'email': 'testuser@testuser.com',
                                     'website': 'http://www.testuser.com',
                                     'picture': image})
        except:
            try:
                response = self.client.post(reverse('rango:register'),
                                        {'username': 'testuser', 'password': 'test1234',
                                         'email': 'testuser@testuser.com',
                                         'website': 'http://www.testuser.com',
                                         'picture': image})
            except:
                return False

        # Check user was successfully registered
        self.assertIn('Thank you for registering!'.lower(), response.content.lower())
        user = User.objects.get(username='testuser')
        user_profile = UserProfile.objects.get(user=user)
        path_to_image = './media/profile_images/testuser.jpg'

        # Check file was saved properly
        self.assertTrue(os.path.isfile(path_to_image))

        # Delete fake file created
        default_storage.delete('./media/profile_images/testuser.jpg')
