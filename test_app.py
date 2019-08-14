from app import get_message


def test_message():
    response = get_message('장소')
    assert response.type == 'location'

    response = get_message('메뉴')
    assert response.type == 'template'
    assert response.alt_text == 'Welcome!'

    response = get_message('프로그램')
    assert response.type == 'template'

    response = get_message('절대 안 나올 것 같은 질의')
    assert response.type == 'text'
