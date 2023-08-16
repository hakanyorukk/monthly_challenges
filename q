[1mdiff --git a/challenges/urls.py b/challenges/urls.py[m
[1mindex effb2ce..2230b3d 100644[m
[1m--- a/challenges/urls.py[m
[1m+++ b/challenges/urls.py[m
[36m@@ -4,6 +4,6 @@[m [mfrom.import views[m
 [m
 urlpatterns = [[m
     path("", views.StartingPageView.as_view(), name="index"), #starting page[m
[31m-    path("/month/<slug>", views.MonthlyChallenge.as_view(), name="month_challenge") #reverse functions,#urltags, dynamic url[m
[32m+[m[32m    path("months/<slug:slug>", views.monthly_challenge, name="month_challenge") #reverse functions,#urltags, dynamic url[m
     #path("accepted/challenges", views.AcceptedChallenges.as_view(), name="challenges")[m
 ][m
\ No newline at end of file[m
