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
