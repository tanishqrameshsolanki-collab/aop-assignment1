# API inventory (redacted)

Supabase project ref and keys are omitted. "Runtime" = seen in this session's browser traffic; everything else is static (bundle) evidence. No endpoint was called directly by the agent.

## Observed at runtime
| Operation | Kind | Inputs | Output shape |
|---|---|---|---|
| `get_featured_explore_projects` | RPC | — | project cards |
| `get_published_project_viewer_branding` | RPC | `p_project_id` | `[{org_id, logo_url, watermark_required, custom_branding_enabled, white_label_enabled}]` |
| `get_public_project_for_viewer` | RPC | `p_project_id` | `{id, name, description, thumbnail, views, status, published_version, published_at, location, feature_flags{gaussian_splat,maps,panorama,media_gallery}, design, published_design, organizations{logo_url}, …}` (see data-model.md) |
| `tour-analytics` | Edge fn (POST) | `action, projectId, publishedVersion, tourType, deviceType, trafficSource, accessSessionToken, protocolVersion` | `{published_version, analytics_session_id, analytics_session_token, attention{serverTime, manifestVersion, protocolVersion, algorithmVersion:'viewport-stencil-3x3-v1', collectionEnabled}}` |
| `assets.realhorizons.ai/thumbnails/*.webp` | CDN | — | images |

## Static only: RPCs (45)
Splat jobs: `create_splat_job_with_billing, quote_splat_job_client, cancel_splat_job, get_splat_job_queue_position, get_splat_queue_depth, update_splat_job_{name,output_file,email_notifications}, link_splat_job_to_project, request_splat_asset_processing, get_splat_asset_processing_job, get_all_splat_jobs_admin`.
Publishing/projects: `publish_project_with_entitlements, get_public_projects, get_featured_explore_projects, get_public_project_for_viewer, get_published_project_viewer_branding`.
Storage: `finalize_storage_upload, abort_storage_upload`.
Org/billing: `get_organization_entitlements, get_organization_members_with_email, get_subscription_plans, get_credit_balance, get_credit_transactions, respond_to_subscription_cancellation_survey, is_super_admin`.
Analytics: `get_all_analytics, get_org_trend`.
AI: `list_ai_usage_jobs, get_ai_usage_job, tour_ai_remove_knowledge_document`.
Onboarding/feed: `get_onboarding_status, complete_onboarding, record_*_event (5), get_capture_guide_completions, sync_local_capture_guide_completion, list_studio_notification_feed, get_studio_notification_summary, mark_studio_feed_seen, get_shared_flight_plan`.

## Static only: tables (25)
`projects, project_analytics, splat_jobs, storage_files, floorplan_assets, skybox_templates, user_hotspot_visual_templates, flight_plans, property_enquiries, organizations, organization_members, organization_invites, organization_ai_guide_entitlements, organization_real_estate_entitlements, users, user_profiles, v_invites_with_inviter, tour_ai_guides, tour_ai_knowledge_documents, tour_ai_sessions, tour_ai_session_analyses, tour_ai_tool_events, tour_ai_transcript_segments, studio_notifications, studio_release_notes, studio_release_note_reads`.

## Static only: edge functions (~30)
Uploads/assets: `request-upload, request-splat-upload, delete-file, delete-prefix, delete-splat-job, list-lod-files, duplicate-tour`. AI: `get-spatial-sense-annotations, promote-spatial-sense-narration, tour-ai-index, studio-assistant-chat`. Maps: `get-google-tiles-root`. Sharing/analytics: `tour-analytics, tour-share-access, analytics-share-access, property-enquiry`. Billing: `dodo-create-checkout, dodo-create-subscription-checkout, dodo-credit-products, dodo-customer-portal, dodo-manage-subscription`. Account: `account-deletion, desktop-auth-code, capture-user-signup-location, founder-email-enqueue, send-contact-email, submit-studio-feedback, studio-feedback-status`.
