from codebase.Sale import Sale

def test_sale_creation():
    sale = Sale(sale_id=1, customer_id=101, stage="Prospect", amount=1000, notes="Initial discussion")

    assert sale.sale_id == 1
    assert sale.customer_id == 101
    assert sale.stage == "Prospect"
    assert sale.amount == 1000
    assert sale.notes == "Initial discussion"

def test_get_sale_id():
    sale = Sale(sale_id=1, customer_id=101, stage="Prospect", amount=1000)
    assert sale.get_sale_id() == 1

def test_set_sale_id():
    sale = Sale(sale_id=1, customer_id=101, stage="Prospect", amount=1000)
    sale.set_sale_id(2)
    assert sale.get_sale_id() == 2

def test_get_customer_id():
    sale = Sale(sale_id=1, customer_id=101, stage="Prospect", amount=1000)
    assert sale.get_customer_id() == 101

def test_set_customer_id():
    sale = Sale(sale_id=1, customer_id=101, stage="Prospect", amount=1000)
    sale.set_customer_id(102)
    assert sale.get_customer_id() == 102

def test_get_stage():
    sale = Sale(sale_id=1, customer_id=101, stage="Prospect", amount=1000)
    assert sale.get_stage() == "Prospect"

def test_set_stage():
    sale = Sale(sale_id=1, customer_id=101, stage="Prospect", amount=1000)
    sale.set_stage("Negotiation")
    assert sale.get_stage() == "Negotiation"

def test_get_amount():
    sale = Sale(sale_id=1, customer_id=101, stage="Prospect", amount=1000)
    assert sale.get_amount() == 1000

def test_set_amount():
    sale = Sale(sale_id=1, customer_id=101, stage="Prospect", amount=1000)
    sale.set_amount(1500)
    assert sale.get_amount() == 1500

def test_get_notes():
    sale = Sale(sale_id=1, customer_id=101, stage="Prospect", amount=1000, notes="Initial discussion")
    assert sale.get_notes() == "Initial discussion"

def test_set_notes():
    sale = Sale(sale_id=1, customer_id=101, stage="Prospect", amount=1000)
    sale.set_notes("Follow-up meeting scheduled")
    assert sale.get_notes() == "Follow-up meeting scheduled"

def test_str_representation():
    sale = Sale(sale_id=1, customer_id=101, stage="Prospect", amount=1000, notes="Initial discussion")
    expected_str = "Sale ID: 1, Customer ID: 101, Stage: Prospect, Amount: 1000, Notes: Initial discussion"
    assert str(sale) == expected_str

