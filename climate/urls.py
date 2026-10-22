from django.urls import path
from . import views

urlpatterns = [
    # Landing page (homepage)
    path('', views.landing_page, name='landing'),
    
    # Authentication pages
    path('login/', views.login_page, name='login'),
    path('verify-email/', views.verify_email_page, name='verify_email'),
    path('verify-phone/', views.verify_phone_page, name='verify_phone'),
    
    # Profile pages
    path('create-profile/', views.create_profile_page, name='create_profile'),
    path('profile/', views.profile_page, name='profile'),
    
    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),
        # ===== AUTOMATION URLs (6 files) =====
    path('automation/custom-task/', views.automation_custom_task, name='automation_custom'),
    path('automation/harvest-detail/', views.automation_harvest_detail, name='automation_harvest'),
    path('automation/irrigation-detail/', views.automation_irrigation_detail, name='automation_irrigation'),
    path('api/get-irrigation-data/', views.api_get_irrigation_data, name='api_get_irrigation_data'),
    path('automation/pest-detail/', views.automation_pest_detail, name='automation_pest'),
    # path('api/get-pest-risk/', views.api_get_pest_risk, name='api_get_pest_risk'),
    path('automation/planting-detail/', views.automation_planting_detail, name='automation_planting'),
    path('api/get-planting-cycles/', views.api_get_planting_cycles, name='api_get_planting_cycles'),
    path('automation/smart-task/', views.automation_smart_task, name='automation_smart'),
    
    # ===== MONITORING URLs (5 files) =====
    path('monitoring/climate-detail/', views.monitoring_climate_detail, name='monitoring_climate'),
    path('monitoring/', views.monitoring_main, name='monitoring'),
    path('monitoring/rainfall-detail/', views.monitoring_rainfall_detail, name='monitoring_rainfall'),
    path('api/predict-rain-live/', views.api_predict_rainfall_live, name='api_predict_rain_live'), # NEW: Dynamic API Endpoint
    #path('monitoring/weather-detail/', views.monitoring_weather_detail, name='monitoring_weather'),
    path('analytics-weather/', views.weather_analytics_view, name='analytics_weather'),
    path('monitoring/yield-detail/', views.monitoring_yield_detail, name='monitoring_yield'),
    
    # ===== SECTOR FINANCIAL URLs (5 files) =====
    path('finance/forecast/', views.finance_forecast, name='finance_forecast'),
    path('api/forecast-data/', views.api_predict_forecast, name='api_predict_forecast'),
    path('finance/ledger/', views.finance_ledger, name='finance_ledger'),
    path('finance/market/', views.finance_market, name='finance_market'),
    path('api/market-data/', views.get_market_data, name='api_market_data'),
    path('finance/roi/', views.finance_roi, name='finance_roi'),
    path('api/predict-roi/', views.api_predict_roi, name='api_predict_roi'),
    path('finance/', views.sector_financial_main, name='finance'),

     # ===== AI-PREDICTION URLS (7 files) =====
    path('ai/chat/', views.ai_chat, name='ai_chat'),
    path('ai/crop-recommend/', views.ai_crop_rec, name='ai_crop_rec'),
    path('api/predict-crop/', views.api_predict_crop, name='api_predict_crop'),
    path('ai/health/', views.ai_health, name='ai_health'),
    # System Health Endpoints
    path('api/system-health/', views.api_system_health, name='api_system_health'),
    path('api/retrain-model/', views.api_retrain_model, name='api_retrain_model'),
    path('ai/soil/', views.ai_soil, name='ai_soil'),
    # Add this underneath your other API endpoints
    path('api/analyze-soil/', views.api_analyze_soil, name='api_analyze_soil'),
    path('ai/suitability/', views.ai_suitability, name='ai_suitability'),
    # Add this underneath your other API endpoints
    path('api/simulate-suitability/', views.api_simulate_suitability, name='api_simulate_suitability'),
    path('ai/image-main/', views.AI_image_main, name='ai_image_main'),
    path('ai/vision/', views.ai_vision, name='ai_vision'),

    # ===== ADVANCED SECTOR URLs =====
    path('advanced/offline/', views.adv_offline, name='adv_offline'),
    path('api/sync-offline/', views.api_sync_offline, name='api_sync_offline'),
    path('advanced/reports/', views.adv_reports, name='adv_reports'),
    path('api/generate-report/', views.api_generate_report, name='api_generate_report'),
    path('advanced/rotation/', views.adv_rotation, name='adv_rotation'),
    # Add these to your ADVANCED SECTOR URLs
    path('advanced/rotation/', views.adv_rotation_page, name='adv_rotation'),
    path('api/rotation-plan/', views.api_generate_rotation, name='api_rotation_plan'),
    path('advanced/satellite/', views.adv_satellite, name='adv_satellite'),
    # ===== ADVANCED SECTOR URLs =====
    path('advanced/satellite/', views.adv_satellite_page, name='adv_satellite'),
    path('api/satellite-ndvi/', views.api_fetch_ndvi, name='api_satellite_ndvi'),
    path('advanced/simulation/', views.adv_simulation, name='adv_simulation'),
    path('api/run-simulation/', views.api_run_simulation, name='api_run_simulation'),
    path('advanced/', views.sector_advanced_main, name='adv_main'),
]