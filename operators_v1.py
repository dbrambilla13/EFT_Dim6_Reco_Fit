operator = {}

operator['cHDD'] = {
                    'variables' : ('jetpt1VSmjj','etaj1VSmjj','detajjVSmjj','pt1VSmjj',),
                    'range' : (-30,30)
}

operator['cHWB'] = {
                    'variables' : ('jetpt1VSmjj','etaj1VSmjj','detajjVSmjj','pt1VSmjj',),
                    'range' : (-100,100)
}

operator['cHW'] = {
                    'variables' : ('pt1VSmjj','pt2VSmjj','mllVSmjj','metVSmjj',),
                    'range' : (-8,8)
}

operator['cHbox'] = {
                    'variables' : ('etaj1VSmjj','jetpt1VSmjj','pt2VSmjj','metVSmjj',),
                    'range' : (-30,30)
}


operator['cHq3'] = {
                    'variables' : ('pt1VSmjj','jetpt1VSmjj','mllVSmjj','detajjVSmjj',), # to be invented
                    'range' : (-5,5)
}

operator['cW'] = {
                    'variables' : ('pt1VSmjj','mllVSmjj','jetpt1VSmjj',), # already known
                    'range' : (-1,1)
}

operator['cll1'] = {
                    'variables' : ('pt1VSmjj','jetpt1VSmjj','mllVSmjj','detajjVSmjj',), # to be invented
                    'range' : (-15,5)
}


operator['cqq11'] = {
                    'variables' : ('etaj1VSmjj','dphijjVSmjj','detajjVSmjj','jetpt1VSmjj',),
                    'range' : (-2,2)
}

operator['cqq1'] = {
                    'variables' : ('etaj1VSmjj','dphijjVSmjj','detajjVSmjj','jetpt1VSmjj',),
                    'range' : (-2,2)
}

operator['cqq31'] = {
                    'variables' : ('etaj1VSmjj','dphijjVSmjj','detajjVSmjj','jetpt1VSmjj',),
                    'range' : (-1.0,1.0)
}

operator['cqq3'] = {
                    'variables' : ('etaj1VSmjj','dphijjVSmjj','detajjVSmjj','jetpt1VSmjj',),
                    'range' : (-1.0,1.0)
}


# missing bsm term!
# operator['cHl1'] = {
#                     'variables' : ('pt1VSmjj','pt2VSmjj','mllVSmjj','metVSmjj',),
#                     'range' : (-100,100)
# }

# not produced
# operator['cHl3'] = {
#                     'variables' : ('pt1VSmjj','jetpt1VSmjj','detajjVSmjj','etaj1VSmjj','metVSmjj',),
#                     'range' : (-2,2)
# }

# not produced
# operator['cHq1'] = {
#                     'variables' : ('jetpt1VSmjj','pt1VSmjj','mllVSmjj','metVSmjj',),
#                     'range' : (-3,3)
# }


# not produced
# operator['cll'] = {
#                     'variables' : ('pt1VSmjj','mllVSmjj','dphijjVSmjj','metVSmjj',),
#                     'range' : (-100,100 )
# }