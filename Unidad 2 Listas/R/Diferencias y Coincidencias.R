Dif_A <- setdiff(ags_loc,jal_loc)
View(Dif_A)
Dif_A2<- setdiff(ags_loc,zac_loc)
View(Dif_A2)
Dif_A3<- setdiff(ags_loc,jal_mun)
View(Dif_A3)
Dif_A4<- setdiff(ags_loc,zac_mun)
View(Dif_A4)
Dif_A5<- setdiff(ags_mun,jal_loc)
View(Dif_A5)
Dif_A6<- setdiff(ags_mun,zac_loc)
View(Dif_A6)
Dif_A7<- setdiff(ags_mun,jal_mun)
View(Dif_A7)
Dif_A8<- setdiff(ags_mun,zac_mun)
View(Dif_A8)

Co_A1<- intersect(ags_loc,jal_loc)
View(Co_A1)
Co_A2<- intersect(ags_loc,zac_loc)
View(Co_A2)
Co_A3<- intersect(ags_loc,jal_mun)
View(Co_A3)
Co_A4<- intersect(ags_loc,zac_mun)
View(Co_A4)
Co_A5<- intersect(ags_mun,jal_loc)
View(Co_A5)
Co_A6<- intersect(ags_mun,zac_loc)
View(Co_A6)
Co_A7<- intersect(ags_mun,jal_mun)
View(Co_A7)
Co_A8<- intersect(ags_mun,zac_mun)
View(Co_A8)