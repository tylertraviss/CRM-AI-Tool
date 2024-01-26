from codebase.Interaction import Interaction

def test_interaction_creation():
    interaction = Interaction(interaction_id=1, timestamp="2022-01-01 12:00:00", interaction_type="Meeting", notes="Discussion about project")
    
    assert interaction.interaction_id == 1
    assert interaction.timestamp == "2022-01-01 12:00:00"
    assert interaction.interaction_type == "Meeting"
    assert interaction.notes == "Discussion about project"

def test_get_interaction_id():
    interaction = Interaction(interaction_id=1, timestamp="2022-01-01 12:00:00", interaction_type="Meeting", notes="Discussion about project")
    assert interaction.get_interaction_id() == 1

def test_set_interaction_id():
    interaction = Interaction(interaction_id=1, timestamp="2022-01-01 12:00:00", interaction_type="Meeting", notes="Discussion about project")
    interaction.set_interaction_id(2)
    assert interaction.get_interaction_id() == 2

def test_get_timestamp():
    interaction = Interaction(interaction_id=1, timestamp="2022-01-01 12:00:00", interaction_type="Meeting", notes="Discussion about project")
    assert interaction.get_timestamp() == "2022-01-01 12:00:00"

def test_set_timestamp():
    interaction = Interaction(interaction_id=1, timestamp="2022-01-01 12:00:00", interaction_type="Meeting", notes="Discussion about project")
    interaction.set_timestamp("2022-01-02 14:00:00")
    assert interaction.get_timestamp() == "2022-01-02 14:00:00"

def test_get_interaction_type():
    interaction = Interaction(interaction_id=1, timestamp="2022-01-01 12:00:00", interaction_type="Meeting", notes="Discussion about project")
    assert interaction.get_interaction_type() == "Meeting"

def test_set_interaction_type():
    interaction = Interaction(interaction_id=1, timestamp="2022-01-01 12:00:00", interaction_type="Meeting", notes="Discussion about project")
    interaction.set_interaction_type("Call")
    assert interaction.get_interaction_type() == "Call"

def test_get_notes():
    interaction = Interaction(interaction_id=1, timestamp="2022-01-01 12:00:00", interaction_type="Meeting", notes="Discussion about project")
    assert interaction.get_notes() == "Discussion about project"

def test_set_notes():
    interaction = Interaction(interaction_id=1, timestamp="2022-01-01 12:00:00", interaction_type="Meeting", notes="Discussion about project")
    interaction.set_notes("Project update")
    assert interaction.get_notes() == "Project update"
