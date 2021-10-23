from thefuzz import fuzz


def SearchRestaurant(restaurant_list, input):
    for i in restaurant_list:
        if fuzz.token_set_ratio(i, input) == 100:
            return i
    print("Your search - " + input + """ - did not match any restaurants.\n
Suggestions:\n
Make sure all words are spelled correctly.\n
Try different keywords.\n
Try more general keywords.""")
    return None


restaurant_list = ["Shake Shack", "Jane's Kitechen", "A.S.K Tea"]
input = "boba"
SearchRestaurant(restaurant_list, input)
