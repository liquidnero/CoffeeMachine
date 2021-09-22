import output
import menu

def test_false():
  test_selection = "test"
  assert output.main(test_selection) == False, "Should be False"

def test_espresso():
  test_selection = "espresso"
  assert output.main(test_selection)[0] == menu.MENU['espresso']['ingredients'], "Should be espresso"
  assert output.main(test_selection)[1] == menu.MENU['espresso']['cost'], "Should be espresso"

if __name__ == "__main__":
    test_false()
    test_espresso()
    print("Everything passed")