import netCDF4 as nc

# directory
fn = './data/plotting-exercise/SST_ERA5_201301.nc'
# read file
ds = nc.Dataset(fn)
print(type(ds))

# print metadata
for var in ds.variables.values():
    print(var)