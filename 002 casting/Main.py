## INTEGER
print("====INTEGER====")
data_int = 9;
print("data = ", data_int, ", type =",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

## FLOAT
print("====FLOAT====")
data_float = 9.5;
print("data = ", data_float, ", type =",type(data_float))

data_int = int(data_float) #akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai int = 0
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

## BOOLEAN
print("====BOOLEAN====")
data_bool = 9.5;
print("data = ", data_bool, ", type =",type(data_bool))

data_int = int(data_bool) #akan dibulatkan ke bawah
data_str = str(data_bool)
data_float = bool(data_bool) #akan false jika nilai int = 0
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_float, ",type =",type(data_float))

## STRING
print("====STRING====")
data_str = 'ucup';
print("data = ", data_str, ", type =",type(data_str))

# data_int = int(data_str) #akan dibulatkan ke bawah harus angka
data_bool = str(data_str)
data_float = bool(data_str) #false jika string kosong
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_bool, ",type =",type(data_bool))
print("data = ", data_float, ",type =",type(data_float))