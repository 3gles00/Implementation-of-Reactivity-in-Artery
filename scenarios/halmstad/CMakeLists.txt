add_opp_run(halmstad CONFIG omnetpp.ini)
add_opp_test(halmstad SUFFIX inet SIMTIME_LIMIT 200s)
add_opp_test(halmstad SUFFIX veins CONFIG veins SIMTIME_LIMIT 200s)
add_opp_test(halmstad SUFFIX repeat CONFIG repeat)