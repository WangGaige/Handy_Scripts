########################data analysis################################
import pandas as pd

a_dataframe = pd.read_csv(FILEPATH)

import seaborn as sns

.shape
.columns
.dtypes
.head() / tail()

listings_df.isnull().sum()

columns_to_drop = ['id', 'host_name', 'last_review']
listings_df.drop(columns_to_drop, axis="columns", inplace=True)

listings_df.fillna({'reviews_per_month': 0}, inplace=True)

listings_df['name'] # => Series
# or
listings_df[['name', 'neighbourhood_group', 'price']] # => DataFrame

listings_df[5:10]

listings_df['price'] < 100

listings_df[listings_df['price'] < 100]

listings_df.nlargest(10, 'number_of_reviews')

listings_df['neighbourhood_group'].unique()

listings_df['neighbourhood_group'].value_counts()

listings_df['neighbourhood'].value_counts().head(10)

listings_df['neighbourhood'].value_counts().head(10).plot(kind='bar')

sns.countplot(data=listings_df, x='neighbourhood_group')

order = listings_df['neighbourhood_group'].value_counts().index
sns.countplot(data=listings_df, x='neighbourhood_group', order=order)

listings_df['room_type'].unique()
sns.countplot(data=listings_df, x="neighbourhood_group", hue="room_type")


sns.distplot(listings_df['price'])

affordable_df = listings_df[listings_df['price'] <= 500]
sns.distplot(affordable_df['price'])

listings_df.price.mean()
affordable_df.price.mean()

sns.violinplot(data=affordable_df, x="neighbourhood_group", y="price")

from matplotlib import pyplot as plt

plt.figure(figsize=(15, 8))

affordable_df.plot(
    kind='scatter',
    x='longitude',
    y='latitude',
    c='price',
    cmap='inferno',
    colorbar=True,
    alpha=0.8,
    figsize=(12,8))
    
    
background_image = plt.imread('https://raw.githubusercontent.com/lewagon/data-images/master/workshops/Neighbourhoods_New_York_City_Map.png')
plt.imshow(background_image, zorder=0, extent=[-74.258, -73.7, 40.49, 40.92])
ax = plt.gca()
affordable_df.plot(
  ax=ax,
  zorder=1,
  kind='scatter',
  x='longitude',
  y='latitude',
  c='price',
  cmap='inferno',
  colorbar=True,
  alpha=0.8,
  figsize=(12,8)
)

import requests

url = "https://..."
response = requests.get(url) # `GET` HTTP request
print(response.status_code)  # Should be 200 if OK
data = response.json()

# TODO: Load `data` in a Pandas DataFrame

import requests
from bs4 import BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
# You now can query the `soup` object!
soup.title.string
soup.find('h1')
soup.find_all('a')
# etc...
################################################################################################
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
             
pd.Series([1, 2, 3, 4, 5])

pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")

wine_reviews.shape

wine_reviews.head()

wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()

reviews.country
reviews['country']
reviews['country'][0]

reviews.iloc[0]
reviews.iloc[:, 0]
reviews.iloc[:3, 0]
reviews.iloc[1:3, 0]
reviews.iloc[-5:]
reviews.loc[0, 'country']
reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

reviews.set_index("title")
reviews.country == 'Italy'
reviews.loc[reviews.country == 'Italy']
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
reviews.loc[reviews.country.isin(['Italy', 'France'])]
reviews.loc[reviews.price.notnull()]

reviews['critic'] = 'everyone'
reviews['index_backwards'] = range(len(reviews), 0, -1)


reviews.points.describe()
reviews.taster_name.describe()
reviews.points.mean()
reviews.taster_name.unique()
reviews.taster_name.value_counts()

review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')

review_points_mean = reviews.points.mean()
reviews.points - review_points_mean

reviews.country + " - " + reviews.region_1

reviews.groupby('points').points.count()

reviews.groupby('points').price.min()

reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

reviews.groupby(['country']).price.agg([len, min, max])

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
mi = countries_reviewed.index

countries_reviewed.reset_index()

countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')

countries_reviewed.sort_values(by='len', ascending=False)

countries_reviewed.sort_index()

countries_reviewed.sort_values(by=['country', 'len'])

reviews.price.dtype
reviews.dtypes
reviews.points.astype('float64')
reviews.index.dtype

reviews[pd.isnull(reviews.country)]
reviews.region_2.fillna("Unknown")

reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")

reviews.rename(columns={'points': 'score'})
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')


canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

pd.concat([canadian_youtube, british_youtube])

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
left.join(right, lsuffix='_CAN', rsuffix='_UK')


################################################
# Scalar
x = np.array(6)
print ("x: ", x)
print ("x ndim: ", x.ndim) # number of dimensions
print ("x shape:", x.shape) # dimensions
print ("x size: ", x.size) # size of elements
print ("x dtype: ", x.dtype) # data type

# Vector
x = np.array([1.3 , 2.2 , 1.7])
print ("x: ", x)
print ("x ndim: ", x.ndim)
print ("x shape:", x.shape)
print ("x size: ", x.size)
print ("x dtype: ", x.dtype) # notice the float datatype

# Matrix
x = np.array([[1,2], [3,4]])
print ("x:\n", x)
print ("x ndim: ", x.ndim)
print ("x shape:", x.shape)
print ("x size: ", x.size)
print ("x dtype: ", x.dtype)

# 3-D Tensor
x = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print ("x:\n", x)
print ("x ndim: ", x.ndim)
print ("x shape:", x.shape)
print ("x size: ", x.size)
print ("x dtype: ", x.dtype)

# Functions
print ("np.zeros((2,2)):\n", np.zeros((2,2)))
print ("np.ones((2,2)):\n", np.ones((2,2)))
print ("np.eye((2)):\n", np.eye((2))) # identity matrix
print ("np.random.random((2,2)):\n", np.random.random((2,2)))


x = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
x[:, 1]
x[0:2, 1:3]

x = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
rows_to_get = np.array([0, 1, 2])
cols_to_get = np.array([0, 2, 1])
x[rows_to_get, cols_to_get]

x = np.array([[1, 2], [3, 4], [5, 6]])
x > 2
x[x > 2]

# Basic math
x = np.array([[1,2], [3,4]], dtype=np.float64)
y = np.array([[1,2], [3,4]], dtype=np.float64)
print ("x + y:\n", np.add(x, y)) # or x + y
print ("x - y:\n", np.subtract(x, y)) # or x - y
print ("x * y:\n", np.multiply(x, y)) # or x * y


# Dot product
a = np.array([[1,2,3], [4,5,6]], dtype=np.float64) # we can specify dtype
b = np.array([[7,8], [9,10], [11, 12]], dtype=np.float64)
c = a.dot(b)
print (f"{a.shape} · {b.shape} = {c.shape}")
print (c)

# Sum across a dimension
x = np.array([[1,2],[3,4]])
print (x)
print ("sum all: ", np.sum(x)) # adds all elements
print ("sum axis=0: ", np.sum(x, axis=0)) # sum across rows
print ("sum axis=1: ", np.sum(x, axis=1)) # sum across columns


# Min/max
x = np.array([[1,2,3], [4,5,6]])
print ("min: ", x.min())
print ("max: ", x.max())
print ("min axis=0: ", x.min(axis=0))
print ("min axis=1: ", x.min(axis=1))



# Broadcasting
x = np.array([1,2]) # vector
y = np.array(3) # scalar
z = x + y


a = np.array((3, 4, 5))
b = np.expand_dims(a, axis=1)
c = a + b

a = a.reshape(-1, 1)


x = np.array([[1,2,3], [4,5,6]])
y = np.transpose(x, (1,0)) # flip dimensions at index 0 and 1

x = np.array([[1,2,3,4,5,6]])
y = np.reshape(x, (2, 3))
z = np.reshape(x, (2, -1))


# Unintended reshaping
z_incorrect = np.reshape(x, (x.shape[1], -1))

# Intended reshaping
y = np.transpose(x, (1,0,2))


# Concatenation
y = np.concatenate([x, x], axis=0) # concat on a specified axis


# Stacking
z = np.stack([x, x], axis=0) # stack on new axis

y = np.expand_dims(x, 1) # expand dim 1

y = np.squeeze(x, 1) # squeeze dim 1

