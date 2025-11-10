# Project Overview: Mood-Based Recipe Recommendation Engine

This project implements a multi-phase mood-based food recipe recommendation system aligned with Jira issues SCRUM-262, SCRUM-263, and SCRUM-264.

## SCRUM-262: MVP - Mood Input and Recipe Recommendation Engine
- Mood input interface (backend FastAPI endpoints) for mood submission and recipe retrieval
- Recipe database with mood mappings
- REST API endpoints:
  - `POST /api/recommendations` for mood-based recipe recommendations
  - `GET /api/recipes/{id}` to fetch recipe details
- Security: TLS and input validation
- Performance target: API response under 300ms
- Scalability: designed for container orchestration
- Unit tests for backend and recommendation logic

## SCRUM-263: Post-MVP - User Profile, Mood Detection & Recipe Saving
- User profile management with support for dietary preferences and mood history
- API endpoints:
  - `POST /api/users` to create users
  - `GET /api/users/{id}/preferences` to retrieve dietary preferences
  - Mood history tracking
- Integration placeholder for third-party mood detection APIs
- Recipe saving and history tracking functionalities
- Security: authentication, data encryption, GDPR compliance
- Performance: session management, caching
- Testing: integration and security audits

## SCRUM-264: Future Expansion - Social Sharing, Analytics & Voice Input
- Social sharing platform to share recipes and moods
- Analytics for mood pattern learning
- Voice input support for mood entry
- API endpoints:
  - `POST /api/social/share` to share content
  - `GET /api/social/analytics` for analytics data
  - `POST /api/social/voice-input` for voice input processing
- Security: privacy controls and advanced data protection
- Performance: scalable analytics platform
- Testing: load testing, usability testing, feature validation

---

This documentation summarizes the implemented features and future expansions from the Jira issues for traceability and project clarity.