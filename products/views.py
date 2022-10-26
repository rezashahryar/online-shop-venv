from django.shortcuts import get_object_or_404, reverse
from django.views import generic
from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddToCartProductForm
from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.


# class ProductListView(generic.ListView):
#     # model = Product
#     queryset = Product.objects.filter(active=True)
#     template_name = 'products/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 12


def product_list_view(request):
    products = Product.objects.filter(active=True)
    recents = Product.objects.all().order_by("-datetime_created")[:3]

    lasted = Product.objects.all().order_by("datetime_created")[:3]

    paginator = Paginator(products, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'page_obj': page_obj,
        'recents': recents,
        'lasteds': lasted,
    }
    return render(request, 'products/product_list.html', context)


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        # context['recent'] = Product.objects.filter("-datetime_created")[:3]
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    # def get_success_url(self):
    #     return reverse('products:product_detail')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        return super().form_valid(form)


