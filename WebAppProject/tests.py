from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from WebAppProject.models import Category

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
        self.assertContains(response, '<a href="%s">Find Nearest Gym</a>' % reverse("workoutweb:nearest_gym"), html=True)

class ModelTest(TestCase):
    def get_post(self, title):

        from WebAppProject.models import Post
        try:
            post = Post.objects.get(title=title)
        except Post.DoesNotExist:
            post = None
        return post


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



