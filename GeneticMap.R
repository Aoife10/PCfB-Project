##This script will make a map of the data generated from the python file newfile2.py

#install.packages('ggmap')
#install.packages('ggplot2')
#to install, first go to the terminal and type in R. This will take you into the R program

#import the freshly made data (made in python) to R
data <- read.table("newdata.txt",header=T)


# load the required packages
library(ggplot2)
library(ggmap)


#retrieve the name of the last column (3) in order to use it later for the legend
leg <- colnames(data)[3]


# getting the map and storing it in mapMed

#Use longitude and latitude to make a map of the mediterranean area
#mapMed <- get_map(location = c(-10, 25, 48, 42), zoom = 4,
mapMed <- get_map(location = c(Long = mean(data$Long), Lat = mean(data$Lat)), zoom = 4,
                      maptype = "satellite", scale = 2)


# plotting the map with some points on it

#ggmap: use the stored data to generate the map and get rid of axis
#ggtitle: name the map
#geom_point: place the transparent (alpha) data points at the correct location...
#scale_colour_gradient: ...and colour them according to the data
#and make a legend according to the name of the data
newmap <- ggmap(mapMed,  extent = "device", legend = "right", title = "Na") + ggtitle(paste("Mediterranean data for ", leg, sep = ""))+
  geom_point(data = data, aes(x = data[,1], y = data[,2], colour = data[,3]), size = 3, alpha=0.8, shape=19) + scale_colour_gradient(low = "yellow", high = "red") + guides(colour = guide_colourbar(leg))

#Save the map as a pdf as the name of the desired data
ggsave(paste(leg, ".pdf", sep = ""), newmap)
