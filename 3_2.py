def pesonal_inf(**kwargs):
    return ' '.join(kwargs.values())


print(pesonal_inf(name='Roma', surname='Frigdal', burthdate='23/12/1986', city='Mensk', email='Romfri@gmail.com',
                  phone_number='234-543-3435'))
