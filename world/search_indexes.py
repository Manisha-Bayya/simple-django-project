from haystack import indexes
from .models import City, Countrylanguage, Country


class CityIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/city.txt")

    city_name = indexes.CharField(model_attr="name")

    i_city_name = indexes.NgramField(model_attr="name")
 
    def get_model(self):
        return City

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class CountryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/country.txt")

    country_name = indexes.CharField(model_attr="name")

    i_country_name = indexes.NgramField(model_attr="name")
 
    def get_model(self):
        return Country

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class CountrylanguageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/country_language.txt")

    language_name = indexes.CharField(model_attr="language")

    i_language_name = indexes.NgramField(model_attr="language")
 
    def get_model(self):
        return Countrylanguage

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

