from django.test import TestCase
class Testview(TestCase):
# Create your tests here.
    def tset_create_post(self):
        response = self.client.get('/blog/create_post/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.assertEqual('Create Post - Blog', soup.title.text)
        main_area = soup.find('div' , id='main_area')
        self.assertIn('Create New Post' , main_area.text)
