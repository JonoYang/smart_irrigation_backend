db = DAL('mysql://siadmin:smartirrigation@smart-irrigation.cbe4esse9asq.us-west-1.rds.amazonaws.com/smart_irrigation')

db.define_table('entry',
                Field('julian_time', type = 'string'),
                Field('time', type = 'string'),
                Field('stake_id', type = 'string'),
                Field('sensor_1', type = 'integer'),
                Field('sensor_2', type = 'integer'),
                Field('sensor_3', type = 'integer'),
                Field('temp', type = 'integer'))