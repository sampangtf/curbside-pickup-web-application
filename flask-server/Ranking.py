from googlemap import distance_matrix

def restaurant_rank(restaurants, origin, beta):

    destination_list = [res['siteName'] for res in restaurants]

    _distance_matrix = distance_matrix(origin, destination_list, depature_time = "now")

    ####Getting Travel Time Score
    traveltime_list= [_distance_matrix['rows'][0]['elements'][idx]['duration']['value'] for idx in len(_distance_matrix['rows'][0]['elements'])]
    traveltime_score = list(map(lambda x: 1/x, traveltime_list))
    scaled_traveltime_score = [(float(i) - min (traveltime_score))/(max(traveltime_score) - min(traveltime_score)) for i in traveltime_score]

    ####Getting 
    rating_list = [(res['rating'], res['noRating']) for res in restaurants]
    total_n_rating = sum(rating_list)
    rating_list_norm = [rating * noRating/total_n_rating for rating, noRating in rating_list]
    #rating_list_norm = (restaurants['rating'] * restaurants['n_rating'])/ total_n_rating
    scaled_rating = [(float(i) - min(rating_list_norm))/(max(rating_list_norm)-min(rating_list_norm)) for i in rating_list_norm]

    weighted_score_dict = {}
    for idx, restuarnt in enumerate(restaurants):
        name = destination_list[idx]
        weighted_score = scaled_rating[idx] * scaled_traveltime_score[idx]
        weighted_score_dict['name'] = weighted_score

    sorted_weighted_score_dict = {k:v for k,v in sorted(weighted_score_dict.items(), key=lambda item: item[1])}


    

    