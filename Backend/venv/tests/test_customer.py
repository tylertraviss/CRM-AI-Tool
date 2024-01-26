from codebase.Customer import Customer

def test_customer_creation():

    customer = Customer()
    customer.name = "John Doe"
    customer.email = "john@example.com"
    customer.phone = "123-456-7890"
    customer.company = "XYZ Corp"
    customer.category = "Regular"
    customer.interactions = ["Meeting", "Call"]
    customer.sales = ["Sale1", "Sale2"]
    customer.tags = ["Tag1", "Tag2"]

    assert customer.name == "John Doe"
    assert customer.email == "john@example.com"
    assert customer.phone == "123-456-7890"
    assert customer.company == "XYZ Corp"
    assert customer.category == "Regular"
    assert customer.interactions == ["Meeting", "Call"]
    assert customer.sales == ["Sale1", "Sale2"]
    assert customer.tags == ["Tag1", "Tag2"]


def test_get_tags():
    customer = Customer()
    customer.tags = ["Tag1", "Tag2", "Tag3"]
    assert customer.get_tags() == ["Tag1", "Tag2", "Tag3"]

def test_add_tags():
    customer = Customer()
    customer.add_tags("NewTag")
    assert "NewTag" in customer.tags

def test_get_name():
    customer = Customer()
    customer.name = "John Doe"
    assert customer.get_name() == "John Doe"

def test_add_sale():
    customer = Customer()
    customer.add_sale("NewSale")
    assert "NewSale" in customer.get_sales()

def test_get_sales():
    customer = Customer()
    customer.sales = ["Sale1", "Sale2", "Sale3"]
    assert customer.get_sales() == ["Sale1", "Sale2", "Sale3"]

def test_get_email():
    customer = Customer()
    customer.email = "john@example.com"
    assert customer.get_email() == "john@example.com"

def test_set_email():
    customer = Customer()
    customer.set_email("jane@example.com")
    assert customer.get_email() == "jane@example.com"
