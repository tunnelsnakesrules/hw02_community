from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['just_title'] = 'Страница об автора'
        context['just_text'] = ('Excelsior.')
        return context


class AboutTechView (TemplateView):
    template_name = 'about/tech.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['just_title'] = (
            'Страница об полученнных знаниях,'
            'которые были использованы для создания сайта')
        context['just_text'] = (
            'Основы Python',
            'Django')
        return context
