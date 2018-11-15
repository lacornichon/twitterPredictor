from twitter_collect import tweet_collect_whole, collect_candidate_actuality_tweets,collect_candidate_tweet_activity, strea_filter_candidate, twitter_connection_setup

twitter_api=twitter_connection_setup.twitter_setup()

def main_collect(num_candidate, filepath, queries, twitter_api):
    candidate_queries= tweet_collect_whole.get_candidate_queries(num_candidate,filepath)
    retweet_candidate=collect_candidate_actuality_tweets.get_retweets_of_candidate(num_candidate)
    tweet_from_candidate_search_quereis=collect_candidate_tweet_activity.get_tweets_from_candidates_search_queries(queries,twitter_api)
    flux_candidate=strea_filter_candidate.ecoute_candidate(num_candidate)
    return candidate_queries, retweet_candidate, tweet_from_candidate_search_quereis, flux_candidate
