# Time of Concentration and Lag Time Plugin

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:15pt; font-weight:600;">Time of concentration and lag time plugin</span><span style=" font-size:8pt;"> </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">  </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">In a hydrological modelling framework, this plugin applies different empirical equations to estimate </span><span style=" font-size:8pt; font-style:italic;">time of concentration </span><span style=" font-size:8pt;">and </span><span style=" font-size:8pt; font-style:italic;">lag time</span><span style=" font-size:8pt;">. The plugin works from a shape file provided by the user, typically representing basins. The user assigns the corresponding attributes to the variables required for calculus of such times. Then, based on the provided attributes, the plugin exclusively enables the computable equations in both </span><span style=" font-size:8pt; font-style:italic;">time of concentration</span><span style=" font-size:8pt;"> and </span><span style=" font-size:8pt; font-style:italic;">lag time</span><span style=" font-size:8pt;">, depending on the selected parameters. The table below presents the required parameters for calculating the different equations, also shown below. </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt; font-weight:600; font-style:italic;">Time of concentration: </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">it is the time required for surface runoff from the farthest point of the basin to reach the outlet point is considered, i.e., the time at which the entire hydrographic unit contributes to the flow. For calculation, you can use different formulas that relate to other parameters typical of the basin. For the estimation of time of concentration, it is recommended to use several empirical equations available in the scientific literature, it is considered appropriate to include at least five estimators (SCS, The Soil Conservation Service, 2010). </span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"><br /></p>
<table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" align="center" width="512" cellspacing="0" cellpadding="0">
<tr>
<td width="160" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-weight:600; color:#000000;">Time of concentration</span><span style=" font-size:8pt;"> </span></p></td>
<td width="187" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-weight:600; color:#000000;">Equation</span><span style=" font-size:8pt;"> </span></p></td>
<td width="164" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-weight:600; color:#000000;">Parameters</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">WILLIAMS</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image001.png" # Time of Concentration and Lag Time Plugin

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:15pt; font-weight:600;">Time of concentration and lag time plugin</span><span style=" font-size:8pt;"> </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">  </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">In a hydrological modelling framework, this plugin applies different empirical equations to estimate </span><span style=" font-size:8pt; font-style:italic;">time of concentration </span><span style=" font-size:8pt;">and </span><span style=" font-size:8pt; font-style:italic;">lag time</span><span style=" font-size:8pt;">. The plugin works from a shape file provided by the user, typically representing basins. The user assigns the corresponding attributes to the variables required for calculus of such times. Then, based on the provided attributes, the plugin exclusively enables the computable equations in both </span><span style=" font-size:8pt; font-style:italic;">time of concentration</span><span style=" font-size:8pt;"> and </span><span style=" font-size:8pt; font-style:italic;">lag time</span><span style=" font-size:8pt;">, depending on the selected parameters. The table below presents the required parameters for calculating the different equations, also shown below. </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt; font-weight:600; font-style:italic;">Time of concentration: </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">it is the time required for surface runoff from the farthest point of the basin to reach the outlet point is considered, i.e., the time at which the entire hydrographic unit contributes to the flow. For calculation, you can use different formulas that relate to other parameters typical of the basin. For the estimation of time of concentration, it is recommended to use several empirical equations available in the scientific literature, it is considered appropriate to include at least five estimators (SCS, The Soil Conservation Service, 2010). </span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"><br /></p>
<table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" align="center" width="512" cellspacing="0" cellpadding="0">
<tr>
<td width="160" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-weight:600; color:#000000;">Time of concentration</span><span style=" font-size:8pt;"> </span></p></td>
<td width="187" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-weight:600; color:#000000;">Equation</span><span style=" font-size:8pt;"> </span></p></td>
<td width="164" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-weight:600; color:#000000;">Parameters</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">WILLIAMS</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image001.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td>
<td rowspan="8" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Basin Area</span><span style=" font-size:8pt;"> </span></p>
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Length of the main channel Average slope of the basin</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">KIRPICH</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image002.png" width="118" height="34" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">CLARK</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image003.png" width="128" height="16" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">TEMEZ</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image004.png" width="101" height="32" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">PILGRIM</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image005.png" width="77" height="13" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">VALENCIA Y ZULUAGA</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image006.png" width="101" height="28" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">VENTURA-HERAS</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image006.png" width="101" height="28" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">BRANSBY - WILLIAMS</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image007.png" width="117" height="25" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">SCS</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image008.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Curve number</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">CALIFORNIA CULVERT PRACTICE</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image009.png" width="172" height="28" /><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Height Delta (maximum dimension - minimum dimension)</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">SCS - RANSER</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image010.png" width="156" height="32" /><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Height Delta (maximum dimension - minimum dimension)</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">GIANDOTTI</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image011.png" width="150" height="33" /><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Height Delta (maximum dimension - minimum dimension)</span><span style=" font-size:8pt;"> </span></p></td></tr></table>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">  </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">  </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt; font-weight:600; font-style:italic;">Lag time: </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">it corresponds to the time between precipitation and the maximum flow of the hydrographic unit, representing the rain delay time (Velez &amp; Botero, 2011).This variable depends mainly on the length and unevenness of the channel, in addition, on the geomorphological characteristics of the basin and the magnitude of runoff. </span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"><br /></p>
<table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" align="center" width="489" cellspacing="0" cellpadding="0">
<tr>
<td width="160" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-weight:600; color:#000000;">Lag Time</span><span style=" font-size:8pt;"> </span></p></td>
<td width="164" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-weight:600; color:#000000;">Equation</span><span style=" font-size:8pt;"> </span></p></td>
<td width="164" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-weight:600; color:#000000;">Parameter</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">EAGLESON</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image012.png" width="119" height="30" /><span style=" font-size:8pt;"> </span></p></td>
<td rowspan="3" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Basin area Main channel length Average watershed slope</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">SNYDER</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image013.png" width="119" height="30" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">CHOW</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image014.png" width="67" height="15" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">SCS</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image015.png" width="125" height="38" /><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Curve number</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">PUTMAN</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image016.png" width="120" height="39" /><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Permeability coefficient</span><span style=" font-size:8pt;"> </span></p></td></tr></table>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">  </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt; font-weight:600; font-style:italic;">Results:</span><span style=" font-size:8pt;"> </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">with the purpose of make the results more readable and provide more significant data visualization, the plugin adds the resulted layer to the QGIS view considering a default thematic classification by applying five categories and labelling the most significant method for the estimation of time of concentration and Lag time. The selection of the most significant method is relied on statisticians as mean, standard deviation and trimean. </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">The classification is based on Natural Breaks (Jenks) and shows the times of concentration calculated. This way, a shape file classified into five intervals showing the minimum and highest concentration is added to the view after processing the selected methods. </span><a name="Imagen 1"></a><span style=" font-size:8pt;"> </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Calibri,sans-serif'; font-size:8pt;">To report failures or make suggestions, please contact </span><a href="mailto:joaherrerama@unal.edu.co"><span style=" font-size:8pt; text-decoration: underline; color:#0000ff;">joaherrerama@unal.edu.co</span></a><span style=" font-family:'Calibri,sans-serif'; font-size:8pt;">.</span><span style=" font-size:8pt;"> </span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt; font-weight:600;">References List</span><span style=" font-size:8pt;"> </span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">  </span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">SCS, The Soil Conservation Service. (2010). Chapter 15 Time of Concentration. </span><span style=" font-size:8pt; font-style:italic;">Hydrology National Engineering Handbook</span><span style=" font-size:8pt;">, </span><span style=" font-size:8pt; font-style:italic;">1</span><span style=" font-size:8pt;">, 1-12. </span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">Velez, J., &amp; Botero, A. (2011). Estimación del tiempo de concentración y tiempo de rezago en la cuenca experimental urbana de la quebrada San Luis, Manizales. </span><span style=" font-size:8pt; font-style:italic;">Dyna</span><span style=" font-size:8pt;">, </span><span style=" font-size:8pt; font-style:italic;">78</span><span style=" font-size:8pt;">(65), 58-71. </span></p></body></html>"64" height="26" /><span style=" font-size:8pt;"> </span></p></td>
<td rowspan="8" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Basin Area</span><span style=" font-size:8pt;"> </span></p>
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Length of the main channel Average slope of the basin</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">KIRPICH</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./
  s/clip_image002.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">CLARK</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image003.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">TEMEZ</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image004.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">PILGRIM</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image005.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">VALENCIA Y ZULUAGA</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image006.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">VENTURA-HERAS</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image006.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">BRANSBY - WILLIAMS</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image007.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">SCS</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image008.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Curve number</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">CALIFORNIA CULVERT PRACTICE</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image009.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Height Delta (maximum dimension - minimum dimension)</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">SCS - RANSER</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image010.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Height Delta (maximum dimension - minimum dimension)</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">GIANDOTTI</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image011.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Height Delta (maximum dimension - minimum dimension)</span><span style=" font-size:8pt;"> </span></p></td></tr></table>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">  </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">  </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt; font-weight:600; font-style:italic;">Lag time: </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">it corresponds to the time between precipitation and the maximum flow of the hydrographic unit, representing the rain delay time (Velez &amp; Botero, 2011).This variable depends mainly on the length and unevenness of the channel, in addition, on the geomorphological characteristics of the basin and the magnitude of runoff. </span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"><br /></p>
<table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" align="center" width="489" cellspacing="0" cellpadding="0">
<tr>
<td width="160" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-weight:600; color:#000000;">Lag Time</span><span style=" font-size:8pt;"> </span></p></td>
<td width="164" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-weight:600; color:#000000;">Equation</span><span style=" font-size:8pt;"> </span></p></td>
<td width="164" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-weight:600; color:#000000;">Parameter</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">EAGLESON</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image012.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td>
<td rowspan="3" style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Basin area Main channel length Average watershed slope</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">SNYDER</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image013.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">CHOW</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image014.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">SCS</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image015.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Curve number</span><span style=" font-size:8pt;"> </span></p></td></tr>
<tr>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; font-style:italic; color:#000000;">PUTMAN</span><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="./images/clip_image016.png" width="64" height="26" /><span style=" font-size:8pt;"> </span></p></td>
<td style=" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;">
<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Times New Roman,serif'; font-size:10pt; color:#000000;">Permeability coefficient</span><span style=" font-size:8pt;"> </span></p></td></tr></table>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">  </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt; font-weight:600; font-style:italic;">Results:</span><span style=" font-size:8pt;"> </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">with the purpose of make the results more readable and provide more significant data visualization, the plugin adds the resulted layer to the QGIS view considering a default thematic classification by applying five categories and labelling the most significant method for the estimation of time of concentration and Lag time. The selection of the most significant method is relied on statisticians as mean, standard deviation and trimean. </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">The classification is based on Natural Breaks (Jenks) and shows the times of concentration calculated. This way, a shape file classified into five intervals showing the minimum and highest concentration is added to the view after processing the selected methods. </span><a name="Imagen 1"></a><span style=" font-size:8pt;"> </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Calibri,sans-serif'; font-size:8pt;">To report failures or make suggestions, please contact </span><a href="mailto:joaherrerama@unal.edu.co"><span style=" font-size:8pt; text-decoration: underline; color:#0000ff;">joaherrerama@unal.edu.co</span></a><span style=" font-family:'Calibri,sans-serif'; font-size:8pt;">.</span><span style=" font-size:8pt;"> </span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt; font-weight:600;">References List</span><span style=" font-size:8pt;"> </span></p>
<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">  </span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">SCS, The Soil Conservation Service. (2010). Chapter 15 Time of Concentration. </span><span style=" font-size:8pt; font-style:italic;">Hydrology National Engineering Handbook</span><span style=" font-size:8pt;">, </span><span style=" font-size:8pt; font-style:italic;">1</span><span style=" font-size:8pt;">, 1-12. </span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">Velez, J., &amp; Botero, A. (2011). Estimación del tiempo de concentración y tiempo de rezago en la cuenca experimental urbana de la quebrada San Luis, Manizales. </span><span style=" font-size:8pt; font-style:italic;">Dyna</span><span style=" font-size:8pt;">, </span><span style=" font-size:8pt; font-style:italic;">78</span><span style=" font-size:8pt;">(65), 58-71. </span></p></body></html>
