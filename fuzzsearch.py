from thefuzz import fuzz


def SearchRestaurant(restaurant_list, input):
    result = []
    for i in restaurant_list:
        if fuzz.token_set_ratio(i, input) == 100:
            result.append(i)
    print("Your search - " + input + """ - did not match any restaurants.\n
Suggestions:\n
Make sure all words are spelled correctly.\n
Try different keywords.\n
Try more general keywords.""")
    if len(result) > 0:
        return result
    else:
        return


restaurant_list = ["Shake Shack", "Jane's Kitechen", "A.S.K Tea"]
input = "Shake shack"
print(SearchRestaurant(restaurant_list, input))
