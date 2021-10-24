from googlemap import distance_matrix, best_routes
import copy

def combination_ranking(combinations, origin):
    combinations_copy = copy.deepcopy(combinations)

    total_traveltime_list = []
    traveltime_score_list = []
    weighted_rating_list = []
    routes = []
    for combination in combinations_copy:
        destination_list = [res['siteName'] for res in combination]

        _distance_matrix = distance_matrix(origin=origin, destination_list=destination_list, depature_time = "now")

        ####Getting Travel Time Score
       
        route, total_traveltime = best_routes(origin, destination_list)
        routes.append(route)
        total_traveltime_list.append(total_traveltime)
        traveltime_score_list.append(1 / total_traveltime)

        ####Getting Rating
        descriptions = [res['description'].split('/') for res in combination]
 
        rating_list = [(float(res[-2]), int(res[-1])) for res in descriptions]

        total_norating = sum([norating for rating, norating in rating_list])
        weighted_rating = [rating * (norating/total_norating) for rating, norating in rating_list]
        
        weighted_rating_list.append(sum(weighted_rating))


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

    combination_score = []
    for combination, traveltime, rating in zip(combinations_copy, scaled_traveltime_score, scaled_rating):
        overall_score = 0.5 * rating + 0.5 * traveltime
        combination_score.append(overall_score)
  
   
    # sorted_combinations = [sorted(res, key = res['overall_score']) for res in combinations_copy]
    sorted_combinations = sorted(combinations_copy, key = lambda x: combination_score[combinations_copy.index(x)], reverse =True)
    sorted_combination_score = sorted(combination_score)
    sorted_total_traveltime_list = sorted(total_traveltime_list, key = lambda x: combination_score[total_traveltime_list.index(x)], reverse =True)
    sorted_weighted_rating_list = sorted(weighted_rating_list, key = lambda x: combination_score[weighted_rating_list.index(x)])
    # sorted_weighted_score_dict = {k:v for k,v in sorted(weighted_score_dict.items(), key=lambda item: item[1])}
    
    return sorted_combinations, total_traveltime_list, routes, weighted_rating_list


    

    