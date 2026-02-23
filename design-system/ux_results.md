## UI Pro Max Search Results
**Domain:** ux | **Query:** animation accessibility reduced-motion data-heavy
**Source:** ux-guidelines.csv | **Found:** 5 results

### Result 1
- **Category:** Animation
- **Issue:** Reduced Motion
- **Platform:** All
- **Description:** Respect user's motion preferences
- **Do:** Check prefers-reduced-motion media query
- **Don't:** Ignore accessibility motion settings
- **Code Example Good:** @media (prefers-reduced-motion: reduce)
- **Code Example Bad:** No motion query check
- **Severity:** High

### Result 2
- **Category:** Animation
- **Issue:** Excessive Motion
- **Platform:** All
- **Description:** Too many animations cause distraction and motion sickness
- **Do:** Animate 1-2 key elements per view maximum
- **Don't:** Animate everything that moves
- **Code Example Good:** Single hero animation
- **Code Example Bad:** animate-bounce on 5+ elements
- **Severity:** High

### Result 3
- **Category:** Animation
- **Issue:** Easing Functions
- **Platform:** All
- **Description:** Linear motion feels robotic
- **Do:** Use ease-out for entering ease-in for exiting
- **Don't:** Use linear for UI transitions
- **Code Example Good:** ease-out
- **Code Example Bad:** linear
- **Severity:** Low

### Result 4
- **Category:** Accessibility
- **Issue:** Motion Sensitivity
- **Platform:** All
- **Description:** Parallax/Scroll-jacking causes nausea
- **Do:** Respect prefers-reduced-motion
- **Don't:** Force scroll effects
- **Code Example Good:** @media (prefers-reduced-motion)
- **Code Example Bad:** ScrollTrigger.create()
- **Severity:** High

### Result 5
- **Category:** Sustainability
- **Issue:** Asset Weight
- **Platform:** Web
- **Description:** Heavy 3D/Image assets increase carbon footprint
- **Do:** Compress and lazy load 3D models
- **Don't:** Load 50MB textures
- **Code Example Good:** Draco compression
- **Code Example Bad:** Raw .obj files
- **Severity:** Medium

