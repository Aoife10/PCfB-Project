d <- read.table("newdataHI.txt", header = T)


#==========================================#
# Create colour gradient human impact map  #
#==========================================#


#install.packages("mapdata")
#install.packages("mapplots")
#install.packages("maps")

# load in relevant packages
library (mapdata)
library (maps)
library (fields)
library (png)


# define ylim and xlim 
xlim <- c(min(d$Long)-1, max(d$Long)+1)
ylim <- c(min(d$Lat)-12.9, max(d$Lat)+12.9)


# Tps() function from fields package
x <- cbind(d$Long, d$Lat)
y <- d[,3]

# Legend name
leg = colnames(d)[3]


# use the tps function to fit the impacts
fit<- Tps(x,y, lambda=0)
# size and legend of png
png(paste("HumanImpacts_", leg, sep = ""),height=1000,width=1000)

# creating gradient
surface(fit, xlim=xlim, ylim=ylim, xlab= "Longitude", ylab="Latitude", 
        main= paste("Human impacts of ", leg, sep = ""))
# adding map
map('worldHires', add=TRUE, fill=TRUE, col='white', boundary='black', lwd = 2)


#add points
points(cbind(d$Long, d$Lat), pch=16, cex=d$Ho*10, col = alpha("black",0.8)) 
dev.off()



