#!/usr/bin/python3

import pymysql

db = pymysql.connect("172.30.195.3", "root", "Admin_123456")

cursor = db.DictCursor()

sql = "select count(*) from sinotrans_core.order_item where month(created_on)>=1 and year(created_on)=2018 " \
      "and item_status = 9"
cursor.execute(sql)
data = cursor.fetchone()
total = data[0]
print(total)
for i in range(0, total, 1000):
    start = i
    step = 1000
    sql = "SELECT * from sinotrans_core.order_item where month(created_on)>=1 and year(created_on)=2018 limit %s,%s"
    cursor.execute(sql, (start, step))
    data = cursor.fetchall()
    for d in data:
        sql = "select * from sinotrans_core.order_info where id = %s "
        cursor.execute(sql, (d['order_id']))
        o = cursor.fetchone()
        print(o)
        sql = "select * from sinotrans_core.order_history where item_id = %s order by created_on desc "
        cursor.execute(sql, (d['id']))
        his = cursor.fetchall()
        for h in his:
            if h['status'] == 5:
                start_on = h['created_on']
            if h['status'] == 4:
                accept_on = h['created_on']
            if h['status'] == 3:
                c_publish_on = h['created_on']
            if h['status'] == 22:
                b_publish_on = h['created_on']
            if h['status'] == 21:
                a_publish_on = h['created_on']
        # sql = "insert into sinotrans_chart.order_analysis (" \
        #       "item_id,order_type,order_code,item_code,lading_num,s_user_id," \
        #       "s_user_name,s_biz_id,s_biz_name,t_user_id,t_biz_id,t_biz_name,order_status,item_status,truck_id,truck_info," \
        #       "driver_id,driver_info,driver_phone,item_weight,container_size,container_shape,container_count,standard_price," \
        #       "total_price,final_total_price,ori_price,actual_price,final_actual_price,order_source,container_yard_id," \
        #       "container_yard,container_stat_id,container_stat,coordinate,stat_coordinate,complete_type,created_on," \
        #       "accept_type,a_publish_on,b_publish_on,c_publish_on,accept_on,start_on,completed_on) " \
        #       "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # cursor.execute(sql, (
        # d['id'], o['order_type'], o['order_code'], d['item_code'], o['lading_num'], o['s_user_id'], o['s_user_name'],
        # o['s_biz_id'], o['s_biz_name'], d['t_user_id'], d['t_biz_id'], d['t_biz_name'],
        # o['order_status'], d['item_status'], d['truck_id'], d['truck_info'], d['driver_id'],
        # d['driver_info'], d['driver_phone'], d['item_weight'], d['container_size'], d['container_shape'],
        # d['container_count'], d['standard_price'], o['total_price'], o['final_total_price'], d['ori_price'],
        # d['actual_price'], d['final_actual_price'], o['order_source'], o['container_yard_id'], o['container_yard'],
        # o['container_stat_id'], o['container_stat'], o['coordinate'], o['stat_coordinate'],
        # d['complete_type'], d['created_on'], d['accept_type'], a_publish_on, b_publish_on, c_publish_on,
        # accept_on, start_on, d['completed_on']))
        # db.commit()
db.close()
