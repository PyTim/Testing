#coding:utf-8
import boto
from boto.s3.connection import OrdinaryCallingFormat
from boto.s3.key import Key

conn = boto.connect_s3('','',host='localhost',is_secure=False,port=88888,calling_format=OrdinaryCallingFormat())

# create bucket
# bucket name can not include upper character
# if bucket already exists, not create again
mybucket = conn.create_bucket('timbucket')
print mybucket.name


#query all bucket 
for mybucket in conn.get_all_buckets():
	print "{name}\t{created}".format(
                name = mybucket.name,
                created = mybucket.creation_date,
        )
#create bucket
mybucket = conn.create_bucket('mybucket001')

#query some one bucket
#get_bucket 添加validate=False表示不检查合法性，即使bucket不存在也会返回这个bucket；
#get_bucket 默认validate=True表示会检查合法性，bucket不存在时候会出现异常404错误；
#look_up是在get_bucket基础上添加了异常处理，如果出现异常则将bucket设置为None;
mybucket =  conn.get_bucket('mybucket001')
print mybucket.name
#print conn.get_bucket('111')
#print conn.get_bucket('111',validate=True) 和上面的效果一样，bucket不存在会出现异常
#print conn.get_bucket('111',validate=False) #始终返回bucket
print conn.lookup('mybucket001') 
#print conn.lookup('bucket003',validate=True) 和上面的效果一样，bucket不存在设置bucket=None
#print conn.lookup('bucket003',validate=False) #始终返回bucket
#总结：所以一般情况下估计应该会使用print conn.lookup('bucket003')，bucket不存在时候返回None

#query the object in the bucket
for key in mybucket.list():
	print key.name
	print key.size
	print key.last_modified


#delete bucket
#方法一：
conn.delete_bucket('mybucket001') 
#方法二：
# mybucket.delete()
#注意：bucket中没有object时候才可以直接删除，否则需要先删除object，然后再删除bucket
for key in mybucket.list():
	key.delete() 
mybucket.delete()

#create an object
mykey = mybucket.new_key('test1.txt')
mykey.set_contents_from_string('testing python boto s3')

#download an object
mykey = mybucket.get_key('test.txt')
mykey.get_contents_to_filename('D:/test111.txt')

#delete one object
mybucket.delete_key('test1.txt')
#delete all object
for key in mybucket.list():
	key.delete() 

















