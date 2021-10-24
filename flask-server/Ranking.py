from googlemap import distance_matrix

def restaurant_rank(search_results, origin, beta):
    
    destinations = 
    #distance_list = list()
    # for idx in range(n_restaurant):
    #     traveltime = distance_matrix['rows'][0]['elements'][idx]['duration']['value']
    #     distance_list.append(traveltime)
    destination_list = search_results['name']
    _distance_matrix = distance_matrix(origin, destination_list, depature_time = "now")
    traveltime_list= [_distance_matrix['rows'][0]['elements'][idx]['duration']['value'] for idx in len(distance_matrix['rows'][0]['elements'])]
    traveltime_score = list(map(lambda x: 1/x, traveltime_list))
    norm_traveltime_score = [(float(i) - min (traveltime_score))/(max(traveltime_score) - min(traveltime_score)) for i in traveltime_score]

    
    total_n_rating = sum(search_results['n_rating'])
    rating = (search_results['rating'] * search_results['n_rating'])/ total_n_rating
    norm_rating = [(float(i) - min(rating))/(max(rating)-min(rating)) for i in rating]

    weighted_score_dict = {}
    for idx, result in enumerate(search_results):
        name = search_results['name']
        weighted_score = norm_rating * norm_traveltime_score
        weighted_score_dict['name'] = weighted_score

    sorted_weighted_score_dict = {k:v for k,v in sorted(weighted_score_dict.items(), key=lambda item: item[1])}


    

    