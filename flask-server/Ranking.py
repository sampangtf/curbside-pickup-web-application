from googlemap import distance_matrix

def combination_ranking(combinations, origin):
    combinations_copy = combinations.deepcopy()
    for restaurants in combinations_copy:
        destination_list = [res['siteName'] for res in restaurants]

        _distance_matrix = distance_matrix(origin=origin, destination_list=destination_list, depature_time = "now")

        ####Getting Travel Time Score
        traveltime_list= [_distance_matrix['rows'][0]['elements'][idx]['duration']['value'] for idx in len(_distance_matrix['rows'][0]['elements'])]
        total_traveltime = sum(traveltime_list)
        #traveltime_score = list(map(lambda x: 1/x, traveltime_list))
        restaurants['total_traveltime'] = total_traveltime
        restaurants['traveltime_score'] = 1 / total_traveltime
        

        ####Getting Rating
        rating_list = [(res['rating'], res['noRating']) for res in restaurants]
        weighted_rating = [rating * (norating/sum(norating)) for rating, norating in rating_list]
        restaurants['weighted_rating'] = weighted_rating
        #rating_list_norm = [rating * noRating/total_n_rating for rating, noRating in rating_list]
        #rating_list_norm = (restaurants['rating'] * restaurants['n_rating'])/ total_n_rating
        
    ######Ranking#######
    scaled_traveltime_score = [(float(restaurants['traveltime_score']) - min(restaurants['traveltime_score'])) \
            /(max(restaurants['traveltime_score']) - min(restaurants['traveltime_score'])) \
            for restaurants in combinations_copy]
    scaled_rating = [(float(restaurants['weighted_rating']) - min(restaurants['weighted_rating'])) \
        /(max(restaurants['weighted_rating'])-min(restaurants['weighted_rating'])) \
            for restaurants in combinations_copy]

    # weighted_score_dict = {}
    for restaurants, traveltime, rating in zip(combinations_copy, scaled_traveltime_score, scaled_rating):
        overall_score = 0.5 * rating + 0.5 * traveltime
        restaurants['overall_score'] = overall_score

    sorted_combinations = [sorted(res, key = res['overall_score']) for res in combinations_copy]
    # sorted_weighted_score_dict = {k:v for k,v in sorted(weighted_score_dict.items(), key=lambda item: item[1])}
    
   
    return sorted_combinations

def combination_ranking(combinations):
    pass

    

    