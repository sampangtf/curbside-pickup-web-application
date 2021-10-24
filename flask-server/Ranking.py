from googlemap import distance_matrix
import copy

def combination_ranking(combinations, origin):
    combinations_copy = copy.deepcopy(combinations)

    total_traveltime_list = []
    traveltime_score_list = []
    weighted_rating_list = []
    for restaurants in combinations_copy:
        destination_list = [res['siteName'] for res in restaurants]

        _distance_matrix = distance_matrix(origin=origin, destination_list=destination_list, depature_time = "now")

        ####Getting Travel Time Score
        traveltime_list= [_distance_matrix['rows'][0]['elements'][idx]['duration']['value'] for idx in range(len(_distance_matrix['rows'][0]['elements']))]
        total_traveltime = sum(traveltime_list)

        total_traveltime_list.append(total_traveltime)
        traveltime_score_list.append(1 / total_traveltime)

        ####Getting Rating
        descriptions = [res['description'].split('/') for res in restaurants]
        print(descriptions)
        rating_list = [(float(res[-2]), int(res[-1])) for res in descriptions]
        print(rating_list)
        total_norating = sum([norating for rating, norating in rating_list])
        weighted_rating = [rating * (norating/total_norating) for rating, norating in rating_list]
        # restaurants['weighted_rating'] = weighted_rating
        print(weighted_rating)
        weighted_rating_list.append(sum(weighted_rating))

        #rating_list_norm = [rating * noRating/total_n_rating for rating, noRating in rating_list]
        #rating_list_norm = (restaurants['rating'] * restaurants['n_rating'])/ total_n_rating
        
    print(total_traveltime_list)
    print(traveltime_score_list)
    print(weighted_rating_list)
    ######Scaling#######
    min_travel_time_score =  min(traveltime_score_list)
    max_travel_time_score = max(traveltime_score_list)
    scaled_traveltime_score = [(float(traveltime_score_list[idx]) - min_travel_time_score) \
            /(max_travel_time_score - min_travel_time_score) \
            for idx, combination in enumerate(combinations_copy)]

    
    max_rating = max(weighted_rating_list)
    min_rating = min(weighted_rating_list)

    scaled_rating = [(float(weighted_rating_list[idx]) - min_rating) \
        /(max_rating - min_rating) \
            for idx, combination in enumerate(combinations_copy)]
    print(scaled_traveltime_score)
    print(scaled_rating)
    combination_score = []
    for combination, traveltime, rating in zip(combinations_copy, scaled_traveltime_score, scaled_rating):
        overall_score = 0.5 * rating + 0.5 * traveltime
        combination_score.append(overall_score)
        print(rating, traveltime)
        print(combination_score)
   
    # sorted_combinations = [sorted(res, key = res['overall_score']) for res in combinations_copy]
    sorted_combinations = sorted(combinations_copy, key = lambda x: combination_score[combinations_copy.index(x)], reverse =True)
    sorted_combination_score = sorted(combination_score)
    sorted_total_traveltime_list = sorted(total_traveltime_list, key = lambda x: combination_score[total_traveltime_list.index(x)], reverse =True)
    sorted_weighted_rating_list = sorted(weighted_rating_list, key = lambda x: combination_score[weighted_rating_list.index(x)])
    # sorted_weighted_score_dict = {k:v for k,v in sorted(weighted_score_dict.items(), key=lambda item: item[1])}
    
    return sorted_combinations, combination_score, total_traveltime_list, weighted_rating_list

def combination_ranking(combinations):
    pass

    

    