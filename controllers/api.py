#/default/put_entry?temp=3&sensor_1=567&sensor_2=123&sensor_3=1010&time=adsf
def put_entry():
    # request.vars is the arguments passed in by the URI
    # 
    # we can get the different values like so:

    julian_time = request.vars.julian_time
    time = request.vars.time
    stake_id = request.vars.stake_id
    temp = request.vars.temp
    sensor_1 = request.vars.sensor_1
    sensor_2 = request.vars.sensor_2
    sensor_3 = request.vars.sensor_3

    # we then put the new entry into the table
    db.entry.insert(julian_time = julian_time, 
                    time = time,
                    stake_id = stake_id,
                    temp = temp, 
                    sensor_1 = sensor_1, 
                    sensor_2 = sensor_2, 
                    sensor_3 = sensor_3)

    # request processed 
    return response.json({'result': 'okay'})

def get_all():
    # get all the stuff from the database, ordered by what ordered they were entered in
    entries = db(db.entry).select(orderby = db.entry.id)
    return response.json(entries)

def get_entry():
    start = request.vars.start
    end = request.vars.end
    entries = db(db.entry.time >= start and db.entry.time <= end).select(orderby = db.entry.time)
    return response.json(entries)