class ResponseData:
 @staticmethod
 def response(module,message,data,status):
  responseData = { 'module' : module, 'message' : message, 'data' : data,'status':status }
  return responseData
                   