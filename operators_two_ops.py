op_couple = {}

op_couple['cqq3_cqq31'] ={
    'op1' : 'cqq3',
    'op2' : 'cqq31',
    'range_op1' : (-2.0,2.0),
    'range_op2' : (-2.0,2.0),
    'variables' : ('jetpt1','detajj','jetpt1VSmjj','detajjVSmjj',),
}

op_couple['cW_cqq1'] ={
    'op1' : 'cW',
    'op2' : 'cqq1',
    'range_op1' : (-2.0,2.0),
    'range_op2' : (-2.0,2.0),
    'variables' : ('jetpt1','pt1','jetpt1VSmjj','pt1VSmjj',),
}

op_couple['cW_cHW'] ={
    'op1' : 'cW',
    'op2' : 'cHW',
    'range_op1' : (- 2.0, 2.0),
    'range_op2' : (-15.0,15.0),
    'variables' : ('pt1','mll','pt1VSmjj','mllVSmjj',),
}

op_couple['cW_cll1'] ={
    'op1' : 'cW',
    'op2' : 'cll1',
    'range_op1' : ( -2.0, 2.0),
    'range_op2' : ( -4.0, 4.0),
    'variables' : ('pt1','jetpt1','pt1VSmjj','jetpt1VSmjj',),
}