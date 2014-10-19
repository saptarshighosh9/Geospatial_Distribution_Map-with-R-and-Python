library(maps)
library(mapdata)
library(mapproj)
library(geosphere)
library(ggmap)

map("worldHires","India",col="blue",fill=TRUE)
points(cod$lon, cod$lat, col = "red", cex = .6)

LA <- c(77.22496,28.635308)
kk <- c(88.36389500000001,22.572646)
gci <- gcIntermediate(LA, kk)
lines(gci, lwd=2, col='red')

> 
cod <- read.csv("test.csv", header = FALSE)
map <- get_map(location = 'India', zoom = 4)
p <- ggmap(map, fullpage = TRUE)
d <- data.frame(lat=cod$V2,lon=cod$V1)
p <- p + geom_point(data=d, aes(lat, lon),color="red", size=3, alpha=0.5)



map <- get_map(location = 'India', zoom = 4)
ggmap(map, fullpage = TRUE)
mapPoints <- ggmap(map) + geom_point(aes(x = cod$lon , y = cod$lat , data = cod, alpha = .5)

get_map(location = c(lon = -95.3632715, lat = 29.7632836),zoom = "auto", scale = "auto",maptype = "terrain",messaging = FALSE, urlonly = FALSE,filename = "ggmapTemp", crop = TRUE,color = c("color", "bw"),source = c("google", "osm", "stamen", "cloudmade"),api_key)





library(ggmap)
library(geosphere)
library(maps)
library(ggplot2)
world = map_data("world","india")
basemap = ggplot(legend = FALSE) + geom_polygon(data = world, aes(x = long,y = lat, group = group, fill = group)) + theme(legend.position = "none")
basemap = basemap + theme(panel.background = element_rect(fill = "#000000"),panel.grid.major = element_blank(), panel.grid.minor = element_blank())
for(n in 0:350)
{
p <- read.csv("test.csv",skip=n,nrows=1,header = FALSE)
d <- data.frame(lon=p$V1,lat=p$V2)
inter = as.data.frame(gcIntermediate(d, c(88.363895,22.572646),n = 50, addStartEnd = TRUE))
names(inter) = c('lon', 'lat')
basemap = basemap + geom_line(data = inter, aes(x = lon, y = lat), color = "blue")
}

