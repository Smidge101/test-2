# Test 1 🧪 1. Initialization Tests
def test_initialization_defaults():
    engine = EngagementEngine("user1")
    assert engine.user_handle == "user1"
    assert engine.score == 0.0
    assert engine.verified is False

def test_initialization_verified():
    engine = EngagementEngine("user2", verified=True)
    assert engine.verified is True


# Test 2 🧪 2. process_interaction Tests
def test_process_like():
    engine = EngagementEngine("user")
    result = engine.process_interaction("like", 3)
    assert result is True
    assert engine.score == 3  # 1 * 3

def test_process_comment():
    engine = EngagementEngine("user")
    engine.process_interaction("comment", 2)
    assert engine.score == 10  # 5 * 2

def test_process_share():
    engine = EngagementEngine("user")
    engine.process_interaction("share", 1)
    assert engine.score == 10

# Tes 3 🧪 3. get_tier Tests
def test_tier_newbie():
    engine = EngagementEngine("user")
    engine.score = 99.9
    assert engine.get_tier() == "Newbie"

def test_tier_influencer_lower_bound():
    engine = EngagementEngine("user")
    engine.score = 100
    assert engine.get_tier() == "Influencer"

def test_tier_influencer_upper_bound():
    engine = EngagementEngine("user")
    engine.score = 1000
    assert engine.get_tier() == "Influencer"

def test_tier_icon():
    engine = EngagementEngine("user")
    engine.score = 1001
    assert engine.get_tier() == "Icon"
