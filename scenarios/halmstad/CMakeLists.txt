add_opp_run(storyboard)
add_opp_test(storyboard SUFFIX inet SIMTIME_LIMIT 200s)
add_opp_test(storyboard SUFFIX veins CONFIG veins SIMTIME_LIMIT 200s)
add_opp_test(storyboard SUFFIX repeat CONFIG repeat)