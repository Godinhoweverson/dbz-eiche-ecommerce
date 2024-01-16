from django.test import TestCase
from django.urls import resolve, reverse
from mainshop import views


class MainshopViewsTest(TestCase):
    
    def test_product_search_view_is_correct(self):
        revolved = resolve(reverse('search'))
        self.assertIs(revolved.func, views.search)

    def test_product_search_loads_correct_template(self):
        response = self.client.get(reverse('search') + '?q=teste')
        self.assertTemplateUsed(response, 'pages/search.html')

    def test_product_search_raises_404_if_no_search_term(self):
        url = reverse('search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_product_search_term_is_on_page_title_and_escaped(self):
        url = reverse('search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )
