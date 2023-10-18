app.UseEndpoints(endpoints =>
{
    endpoints.MapControllerRoute(
        name: "default",
        pattern: "{controller=Home}/{action=Index}/{id?}");
    endpoints.MapControllerRoute(
        name: "prediction",
        pattern: "prediction",
        defaults: new { controller = "Prediction", action = "PredictSurvival" });
});
