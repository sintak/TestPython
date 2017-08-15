s = 'sintak'
d = 10
print('hello %s %d'%(s, d))

##########

import sys, traceback
 
traceback_template = '''Traceback (most recent call last):
 File "%(filename)s", line %(lineno)s, in %(name)s
%(type)s: %(message)s\n''' # Skipping the "actual line" item
 
# Also note: we don't walk all the way through the frame stack in this example
# see hg.python.org/cpython/file/8dffb76faacc/Lib/traceback.py#l280
# (Imagine if the 1/0, below, were replaced by a call to test() which did 1/0.)
 
try:
  1/0
except:
  # http://docs.python.org/2/library/sys.html#sys.exc_info
  exc_type, exc_value, exc_traceback = sys.exc_info() # most recent (if any) by default
 
  '''
  Reason this _can_ be bad: If an (unhandled) exception happens AFTER this,
  or if we do not delete the labels on (not much) older versions of Py, the
  reference we created can linger.
 
  traceback.format_exc/print_exc do this very thing, BUT note this creates a
  temp scope within the function.
  '''
 
  traceback_details = {
             'filename': exc_traceback.tb_frame.f_code.co_filename,
             'lineno' : exc_traceback.tb_lineno,
             'name'  : exc_traceback.tb_frame.f_code.co_name,
             'type'  : exc_type.__name__,
             'message' : exc_value.message, # or see traceback._some_str()
            }
 
  del(exc_type, exc_value, exc_traceback) # So we don't leave our local labels/objects dangling
  # This still isn't "completely safe", though!
  # "Best (recommended) practice: replace all exc_type, exc_value, exc_traceback
  # with sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]
 
 
  ## 修改这里就可以把traceback打到任意地方，或者存储到文件中了
  print(traceback_template % traceback_details)