class arealjoin:
    """ 
    Used to join shapefiles for areal weighting.
    """
    def read1(self, source):
        """
        reads the source shapefile

        Parameters
        ----------
        source : str
            path of the shapefile

        Returns 
        -------
        dataframe

        """
        return 
    
    def read2(self, target):
        """
        reads the target shapefile

        Parameters
        ----------
        target : str
            path of the target shapefile

        Returns
        -------
        dataframe

        """
        pass
    
class areal_weight:
    """
    Calculates Aerial weight and uses exclusion zone.
    """
    def arealjoin(self, source, target):
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
        return

    def arealweight(self, join):
        """
        Calculates areal weight.
        
        Parameters
        ----------
        join : dataframe
            dataframe that has been spatially intersected    
            
        Returns
        -------
        dataframe with new column containing output        
        
        """
        return
