from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField('Name', max_length=50, unique=True, null=False, blank=True)

    def __str__(self):
        return f'{self.name}'


class Note(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='note', null=True, blank=True)

class Meta:
    ordering = ('name',)
    def __str__(self):
        return f'{self.name} ({self.price})'

#
# class Vehicle(models.Model):
#     plate_number = models.CharField(max_length=50, null=False, blank=False)
#     win_number = models.CharField(max_length=50, null=False, blank=False)
#     client = models.CharField(max_length=50, null=False, blank=False)
#     model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.win_number
#
#
# class Order(models.Model):
#     date = models.DateField(null=False, blank=False)
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     order_detail = models
#
#     def __str__(self):
#         return f'{self.vehicle.win_number} ({self.total_price})'
#
#     @property
#     def total_price(self):
#         total_price = 0
#         order_detail = self.order_details.all()
#         for detail in order_detail:
#             total_price += detail.price * detail.quantity
#         return total_price
#
#
# class OrderDetail(models.Model):
#     quantity = models.IntegerField(null=False, blank=False)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, related_name='order_details', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.order.vehicle.model.brand}'
#
#     @property
#     def price(self):
#         return self.service.price
