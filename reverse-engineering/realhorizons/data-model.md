# Data model

## Verified: published project document (`get_public_project_for_viewer`)
```
Project { id, name, description, thumbnail, views, status, location, created_at, published_at,
          published_version:int, org_id, organizations{logo_url},
          feature_flags{gaussian_splat, maps, panorama, media_gallery},
          design: Design, published_design: Design }     // draft vs. immutable snapshot
Design  { tourConfig{template:'property-listing', modules, workflow}, tourDetails{colorTheme, localization…},
          localization{primaryLanguage}, modules{ ai, maps, panorama, mediaGallery, floorplans{version},
          splat3d, spatialTour, propertyTour, lastPublishCost } }
```
Full key/type list: `evidence/project-paths.txt` (1,311 paths).

### Scene (in `spatialTour.scenes[]` / `propertyTour.scenes[]`)
```
Scene { id, name, sortOrder, floorId, navigationMode:'orbit'|'walkthrough', allowThirdPerson,
        movement{mode, source, confirmed},
        splatFile{id, name, url, size, format:'sogs', uploadedAt}, splatTransform, orientation,
        entryCamera{position{x,y,z}, target{x,y,z}, fov},
        setup{groundConfirmed, orientationConfirmed, scaleConfirmed, orbitBoundsConfirmed, openingViewConfirmed},
        sceneSettings{splatType:'interior'|'exterior', quality, lighting, fov, cameraHeight, cameraCollisionDepth,
                      min/maxZoom(+Enabled), backgroundColor, collisionControlsEnabled, enableAdaptiveLabelLimit…},
        lodSettings{isLodFormat, lodDistances[], lodRangeMin, lodRangeMax, colorizeLod},
        revealSettings{enabled, effect}, hdriSource, hdriUrl, backgroundAudio{mode},
        collision{source:'primitives', baseFloor{y}, sectionPlane{axis, offset, offsets{XY,XZ,YZ}, flip},
                  snap{enabled, incrementM}, components[]: CollisionComponent},
        hotspots[]: Hotspot, sprites[]: { reframe{camera{navigationMode}, variants[], display{mode}} } }
Hotspot { id, type:'info'|'navigation', title, description, icon, thumbnailUrl,
          position{x,y,z}, focus{position, target}, targetSceneId, targetSceneType:'3d',
          customization{markerStyle:'billboard'|'mapMarker', shape, color, size, lineHeight, showTextBox, textBoxContent} }
Link    { id, fromSceneId, hotspotId, targetSceneId, targetHotspotId, entryCamera, transitionStyle:'camera-crossfade' }
CollisionComponent { id, name, type:'blocker', preset:'wall'|'polygon', points[{x,z}], position, rotation, size,
                     floorId, locked, visible, wallPathId, wallPathIndex, wallPathName }
Floor   { id, name, level, sortOrder }   // propertyTour.floors[], minimap{enabled, collapsedByDefault}
```
`splat3d` (single-scene mode) additionally holds `cameraState, openingView*, colorAdjustments{10 sliders}, hdriSettings{…}, gizmoSettings{mode, space, visible}, viewerSettings{orbit limits, damping, autoRotate}, pointCloudSettings, presentationMode:'first-person', pendingAnnotationJobId, sourceJobId, sceneEdited`.

## Strongly supported (table names only)
User / UserProfile, Organization (+members, invites, entitlements), Project, ProjectAnalytics, SplatJob, StorageFile, FloorplanAsset (org-scoped), SkyboxTemplate, HotspotVisualTemplate, FlightPlan, PropertyEnquiry, TourAIGuide / KnowledgeDocument / Session / Transcript / ToolEvent / SessionAnalysis, Notification, ReleaseNote.

## Relationships (Inferred)
Organization 1–n Project; Project 1–n SplatJob (via `link_splat_job_to_project`, `sourceJobId`); Project 1–1 draft design + versioned published snapshot; Scene n–1 Floor; Hotspot 1–0..1 Link.
