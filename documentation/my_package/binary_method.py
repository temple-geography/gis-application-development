class clipper:
    """ 
    This can be used to clip the ancillary data to the interest zone
    """
    def getanc(self, source):
        """
        reads the ancillary shapefile

        Parameters
        ----------
        source : str
            name of the ancillary shapefile

        Returns
        -------
        Ancillary dataframe

        """
        ancillary = self.source
        return ancillary
    
    def clipanc(self, ancillary):
        """
        Clips the ancillary data to just the interest zone

        Parameters
        ----------
        ancillary : TYPE
            DESCRIPTION.

        Returns
        -------
        Clipped dataframe

        """
        pass
    
class binaryMethod:
    """
    Calculates Aerial weight and uses exclusion zone.
    """
    def binaryjoin(self, source, target):
        """
        Joins the source and target dataframes

        Parameters
        ----------
        source : dataframe
            source dataframe
            
        target : dataframe
            target dataframe
            
        Returns
        -------
        joined dataframe

        """
        join = 5
        return

    def binaryweight(self, join):
        """
        calculates areal weight based on exclusion zone.
        
        Parameters
        ----------
        join : dataframe
            dataframe that has been spatially intersected    
            
        Returns
        -------
        dataframe with new column containing output        
        
        """
        return