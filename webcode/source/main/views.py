from django.views.generic import TemplateView
from django.shortcuts import render
import accounts.forms
import requests
import common.db_helper

class IndexPageView(TemplateView):
	template_name = 'main/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		# This is just an example of how to query the db to pull information.
		# To use this we just need
		sql = 'SELECT * FROM Stock WHERE TickerSymbol=?'
		arg = ('APPL',)
		record = common.db_helper.db_query(sql, arg)
		if record:
			context['symbol'] = record['TickerSymbol']
		else:
			context['symbol'] = 'Does not exist'

		return context


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
