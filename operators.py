operator = {}

operator['cHDD'] = {
                    'variables' : ('jetpt1','etaj1','detajj','pt1',),
                    'range' : (-10,10)
}

operator['cHWB'] = {
                    'variables' : ('jetpt1','etaj1','detajj','pt1',),
                    'range' : (-10,10)
}

operator['cHW'] = {
                    'variables' : ('pt1','pt2','mll','met',),
                    'range' : (-8,8)
}

operator['cHbox'] = {
                    'variables' : ('etaj1','jetpt1','pt2','met',),
                    'range' : (-2,2)
}


operator['cHq3'] = {
                    'variables' : ('pt1','jetpt1','mll','detajj',), # to be invented
                    'range' : (-5,5)
}

operator['cW'] = {
                    'variables' : ('pt1',), # already known
                    'range' : (-1,1)
}

operator['cll1'] = {
                    'variables' : ('pt1','jetpt1','mll','detajj',), # to be invented
                    'range' : (-20,5)
}


operator['cqq11'] = {
                    'variables' : ('etaj1','dphijj','detajj','jetpt1',),
                    'range' : (-2,2)
}

operator['cqq1'] = {
                    'variables' : ('etaj1','dphijj','detajj','jetpt1',),
                    'range' : (-2,2)
}

operator['cqq31'] = {
                    'variables' : ('etaj1','dphijj','detajj','jetpt1',),
                    'range' : (-1.0,1.0)
}

operator['cqq3'] = {
                    'variables' : ('etaj1','dphijj','detajj','jetpt1',),
                    'range' : (-1.0,1.0)
}


# missing bsm term!
# operator['cHl1'] = {
#                     'variables' : ('pt1','pt2','mll','met',),
#                     'range' : (-100,100)
# }

# not produced
# operator['cHl3'] = {
#                     'variables' : ('pt1','jetpt1','detajj','etaj1','met',),
#                     'range' : (-2,2)
# }

# not produced
# operator['cHq1'] = {
#                     'variables' : ('jetpt1','pt1','mll','met',),
#                     'range' : (-3,3)
# }


# not produced
# operator['cll'] = {
#                     'variables' : ('pt1','mll','dphijj','met',),
#                     'range' : (-100,100 )
# }