### R Script snippets- walkthrough for Kaleo

''' R
Segments of this code are adapted from Zuur, A. F., Ieno, E. N., and Elphick, C. S. 2010. 
A protocol for data exploration to avoid common statistical problems. 
Methods in Ecology and Evolution 1(1): 3 - 14. 
'''

# setwd() # Use this command to tell R where to look for the files
myData <- read.csv("my_predictor_data.csv") # EDIT: read in your predictor (x variable) data

### Load spatial libraries ###
# install.packages() # Use this command to install the packages you are missing 
library(raster)
library(sp)
library(rgdal)
library(dismo)

### Ensure there are no duplicate coordinate pairs; remove any that are identified
coords <- cbind(myData$Longitude, myData$Latitude) # EDIT
coordsSP <- SpatialPoints(coords, proj4string=CRS(as.character(NA)))
zerodist(coordsSP, zero = 0.0)

### Check for troublesome outliers
# Edit that second line, then copy and paste:

library(lattice)
Z <- myData[,c(4:16, 18)] # EDIT: columns 4 - 16 and column 18 included the predictors I wanted to check
dotplot(as.matrix(Z), groups = FALSE,
        strip = strip.custom(bg = 'white',
                             par.strip.text = list(cex = 0.8)),
        scales = list(x = list(relation = "free"),
                      y = list(relation = "free"),
                      draw = FALSE),
        col = 1, cex  = 0.5, pch = 16,
        xlab = "Value of covariate",
        ylab = "Order of the data from file")



### To determine correlations between predictor variables and between each covariate and the response variable, we adapted code from the R Cookbook (page 155) by Paul Teetor (2011). This code produces a useful scatterplot matrix.
# Edit near the end, then you can copy and paste this chunk:

panel.cor <- function(x, y, digits=2, prefix="", cex.cor, ...) {
  usr <- par("usr")
  on.exit(par(usr))
  par(usr = c(0, 1, 0, 1))
  r <- abs(cor(x, y, use="complete.obs"))
  txt <- format(c(r, 0.123456789), digits=digits)[1]
  txt <- paste(prefix, txt, sep="")
  if(missing(cex.cor)) cex.cor <- 1.0/strwidth(txt)
  text(0.5, 0.5, txt, cex = cex.cor * (1 + r) / 2)
}
panel.hist <- function(x, ...) {
  usr <- par("usr")
  on.exit(par(usr))
  par(usr = c(usr[1:2], 0, 1.5) )
  h <- hist(x, plot = FALSE)
  breaks <- h$breaks
  nB <- length(breaks)
  y <- h$counts
  y <- y/max(y)
  rect(breaks[-nB], 0, breaks[-1], y, col="white", ...)
}
# EDIT: change the column numbers to correspond to the predictors you want to check:
pairs(myData[,c(4:16, 18)], upper.panel = panel.cor, diag.panel = panel.hist, lower.panel = panel.smooth) 
myData$UselessColumn <- NULL # to remove a column; remember, remove a predictor frpom pairs with correlations over 70%



### Check for local and global spatial autocorrelation
# You so this after you run your model (if you run one)

# Run a GLM for your crabs

all.model <- glm(Crabs ~ 
                   Chl +
                   HumanPopulation +
                   SST +
                   Slope,
                 data = myData, family = poisson) # for count data, Poisson works

myData <- na.omit(myData) # Remove all rows with NAs to check spatial autocorrelation

# Calculate Moran's I Values explicitly for a certain distance and test for significance
library(spdep)
myData.nb <- dnearneigh(as.matrix(myData[1:2]), 0, 1)

# Turns neighborhood object into weighted list
myData.list <- nb2listw(myData.nb)
MT <- moran.test(residuals(myData), listw=myData.list)
MT

# Calculate Geary's C (a test of local spatial autocorrelation)
# The value of Geary's C lies between 0 and 2. 1 means no spatial autocorrelation. Values lower than 1 demonstrate increasing positive spatial autocorrelation, whilst values higher than 1 illustrate increasing negative spatial autocorrelation.
GC <- geary.test(residuals(myData), listw=myData.list)
GC